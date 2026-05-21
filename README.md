# AWS Serverless Contact Form

A **Serverless Contact Form** project built using **AWS Lambda, API Gateway, and DynamoDB**.  
Users can submit their details (name, email, and message), these submitted datas are stored in DynamoDB.

## Architecture

User --> API Gateway --> Lambda Function --> DynamoDB

In future : Try implementation with SES (email notification)

## Features

- Accepts user input (name, email, message) via API POST request  
- Stores the submitted data in DynamoDB  
- Returns success message to user (notify the change has made)  

## AWS Services Used

- **Lambda**: Serverless function to process data  
- **API Gateway**: HTTP API endpoint for Lambda  
- **DynamoDB**: NoSQL database to store user submissions  
- **IAM**: Permissions for Lambda to access DynamoDB  
- **SES**: (optional): Email notification  

## Function Overview Diagram

<img width="564" height="213" alt="11-function-overview-diagram" src="https://github.com/user-attachments/assets/5ab2605b-f413-4cb7-8c61-073e5d982b0d" />


## How to Test

1. Use **curl** or **Postman** to send a POST request:

```bash
curl -X POST "YOUR_API_GATEWAY_ENDPOINT" \
-H "Content-Type: application/json" \
-d "{\"name\":\"Gopika\",\"email\":\"gopika@example.com\",\"message\":\"Hello world\"}"


2. Check DynamoDB table for new entries as you add
