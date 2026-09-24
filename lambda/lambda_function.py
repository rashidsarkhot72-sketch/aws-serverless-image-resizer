import boto3
import os
import urllib.parse
from PIL import Image
from io import BytesIO

s3 = boto3.client("s3")

OUTPUT_BUCKET = os.environ.get(
    "OUTPUT_BUCKET",
    "rashid-image-resizer-2026-928374"
)


def lambda_handler(event, context):

    for record in event["Records"]:

        source_bucket = record["s3"]["bucket"]["name"]

        source_key = urllib.parse.unquote_plus(
            record["s3"]["object"]["key"]
        )

        print(f"Image uploaded: s3://{source_bucket}/{source_key}")

        response = s3.get_object(
            Bucket=source_bucket,
            Key=source_key
        )

        image_data = response["Body"].read()

        image = Image.open(BytesIO(image_data))

        print(f"Original size: {image.size}")

        # Resize image while keeping aspect ratio
        image.thumbnail((800, 800))

        output = BytesIO()

        image_format = image.format or "JPEG"

        if image_format.upper() == "JPEG":
            image.save(output, format="JPEG", quality=80)
        else:
            image.save(output, format=image_format)

        output.seek(0)

        output_key = f"resized/{source_key}"

        s3.put_object(
            Bucket=OUTPUT_BUCKET,
            Key=output_key,
            Body=output,
            ContentType=response.get(
                "ContentType",
                "image/jpeg"
            )
        )

        print(
            f"Resized image created: "
            f"s3://{OUTPUT_BUCKET}/{output_key}"
        )

    return {
        "statusCode": 200,
        "body": "Image resized successfully"
    }