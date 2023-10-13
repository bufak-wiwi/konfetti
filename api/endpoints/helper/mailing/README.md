# Mailing with Templates

In order to send e-mails, the following requirements must be met:

- The SMTP access data must be stored in the `.env` file.
- A template must be available for the specific e-mail

## SMTP-Settings

The following entries must be present in the .env file:

- SMTP_SERVER
- SMTP_PORT (SSL)
- SMTP_USERNAME
- SMTP_PASSWORD

If you only want to test the mailing, you can set the `SMTP_TESTING=TRUE` entry.  
The generated HTML will then be printed in the console.

## E-Mail Template

To create the templates we use handlebars (https://handlebarsjs.com/).  
The templates must be placed in the folder `helper/mailing/email_templates`.

## Sending the E-Mails

To send a mail afterwards, the function `sendEmail` must be called.
For this to work, it must be imported beforehand `from endpoints.helper.mailing.mailing import sendEmail`  
The function expects the following parameters:

- template - Name of the template without extension(required)
- to - Mail recipient (required)
- subj - Subject of the Mail (required)
- replyTo - Reply to Adress (optional)
- fields - Inputs for the variables in the template (required)

Sample function call:

```python
sendEmail(template="sample",to="testreciupient@test.local", subj="Testmail", replyTo="testeplytp@test.local",fields={"name":"Konfetti User","message":"Thank you for using our system. Have fun."})
```
