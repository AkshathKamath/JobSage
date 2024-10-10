package aws

import (
	"log"
	"net/http"
	"os"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/credentials"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
)

func FileUpload(r *http.Request) bool {

	err := r.ParseMultipartForm(10 << 20)
	if err != nil {
		return false
	}

	file, header, err := r.FormFile("file")
	if err != nil {
		return false
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
		return false
	}

	svc := s3.New(sess)

	key := "Resume.pdf"

	_, err = svc.PutObject(&s3.PutObjectInput{
		Bucket:             aws.String("resumehelp"),
		Key:                aws.String(key),
		Body:               file,
		ContentLength:      aws.Int64(header.Size),
		ContentType:        aws.String("application/pdf"),
		ContentDisposition: aws.String("inline"),
	})
	if err != nil {
		return false
	}

	log.Println("File Upload Successful!")
	return true
}
