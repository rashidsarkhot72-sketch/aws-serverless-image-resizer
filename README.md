\# AWS Serverless Image Resizer



A serverless image resizing project built using \*\*Amazon S3, AWS Lambda, Python, and Pillow\*\*.



\## Project Overview



This project automatically resizes images using an event-driven AWS serverless architecture.



When an image is uploaded to the S3 `uploads/` folder, Amazon S3 triggers an AWS Lambda function. The Lambda function uses Pillow to resize the image and stores the processed image in the `resized/uploads/` folder.



\## Architecture



User

&#x20; |

&#x20; v

Amazon S3

/uploads/

&#x20; |

&#x20; | ObjectCreated Event

&#x20; v

AWS Lambda

image-resizer-2026

&#x20; |

&#x20; v

Pillow

Image Resizing

&#x20; |

&#x20; v

Amazon S3

/resized/uploads/



\## Workflow



1\. Upload an image to the S3 `uploads/` folder.

2\. S3 generates an `ObjectCreated` event.

3\. The event triggers the Lambda function.

4\. Lambda downloads the uploaded image.

5\. Pillow processes and resizes the image.

6\. Lambda uploads the resized image to `resized/uploads/`.

7\. The S3 trigger only monitors the `uploads/` prefix, preventing recursive Lambda execution.



\## AWS Services Used



\- \*\*Amazon S3\*\* – Stores original and resized images.

\- \*\*AWS Lambda\*\* – Runs the image resizing code without managing servers.

\- \*\*Amazon CloudWatch Logs\*\* – Monitors Lambda execution.

\- \*\*AWS IAM\*\* – Provides permissions to Lambda.



\## Technologies Used



\- Python 3.13

\- Pillow 12.2.0

\- AWS CLI

\- Git

\- GitHub



\## Project Structure



aws-serverless-image-resizer/

│

├── lambda/

│   └── lambda\_function.py

│

├── requirements.txt

├── .gitignore

└── README.md

S3 Structure

rashid-image-resizer-2026-928374/

│

├── photo.jpg

│

├── uploads/

│   └── photo.jpg

│

└── resized/

&#x20;   └── uploads/

&#x20;       └── photo.jpg

S3 Trigger Configuration



The Lambda trigger is configured with:



Event: ObjectCreated:\*

Prefix: uploads/



Using the uploads/ prefix prevents the resized image inside resized/ from triggering the Lambda again.



Test Result



The project was successfully tested with an image.



Original Image

Size: 3364 × 3364

File size: 1,974,009 bytes

Resized Image

Location:

s3://rashid-image-resizer-2026-928374/resized/uploads/photo.jpg



File size:

71,975 bytes

Lambda Execution Result



CloudWatch Logs confirmed:



Image uploaded:

s3://rashid-image-resizer-2026-928374/uploads/photo.jpg



Original size:

(3364, 3364)



Resized image created:

s3://rashid-image-resizer-2026-928374/resized/uploads/photo.jpg

Example Workflow

photo.jpg

&#x20;  |

&#x20;  v

S3 /uploads/

&#x20;  |

&#x20;  v

Lambda Trigger

&#x20;  |

&#x20;  v

Pillow Resize

&#x20;  |

&#x20;  v

S3 /resized/uploads/

&#x20;  |

&#x20;  v

Resized photo.jpg

Key Features

Serverless image processing

Automatic S3 event triggering

Image resizing with Pillow

Automatic output storage in S3

CloudWatch logging

IAM-based permissions

No traditional server required

Project Purpose



This project demonstrates an event-driven serverless image processing workflow using AWS services and Python.



Author



Rashid Sarkhot

