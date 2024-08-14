package handlers

import (
	"github.com/gin-gonic/gin"
    "net/http"
	"io/ioutil"
	"bytes"
)

func ScoreHandler(c *gin.Context)  {
	
	requestBody, err := ioutil.ReadAll(c.Request.Body)
    if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to read request body"})
        return
    }
	
	url := "https://resume-help.vercel.app/score"

	response, err := http.Post(url, "application/json", bytes.NewBuffer(requestBody))
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to forward request"})
        return
    }
    defer response.Body.Close()

	responseBody, err := ioutil.ReadAll(response.Body)
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to read response"})
        return
    }

	c.Data(response.StatusCode, response.Header.Get("Content-Type"), responseBody)

}