package handlers

import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/credentials"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/s3"
    "github.com/gin-gonic/gin"
    "net/http"
	"os"
	// "log"
)

func S3UploadHandler(c *gin.Context)  {
	// for name, values := range c.Request.Header {
    // 	for _, value := range values {
    //     	log.Printf("%s: %s", name, value)
    // 	}
	// }

	file, header, err := c.Request.FormFile("file")
    if err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid file"})
        return
    }
    defer file.Close()

	sess, err := session.NewSession(&aws.Config{
        Region: aws.String("us-east-1"),
        Credentials: credentials.NewStaticCredentials(
            os.Getenv("AWS_ACCESS_KEY_ID"),
            os.Getenv("AWS_SECRET_KEY_ID"),
            ""),
    })
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": "Could not create AWS session"})
        return
    }

	svc := s3.New(sess)

	key := "Resume.pdf"

	 _, err = svc.PutObject(&s3.PutObjectInput{
        Bucket:        aws.String("resumehelp"),
        Key:           aws.String(key),
        Body:          file,
        ContentLength: aws.Int64(header.Size),
    })
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": "Could not upload file to S3"})
        return
    }

    c.JSON(http.StatusOK, gin.H{"message": "File uploaded successfully", "fileKey": key})
}