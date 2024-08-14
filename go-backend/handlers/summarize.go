package handlers

import (
	"github.com/gin-gonic/gin"
    "net/http"
	"io/ioutil"
)

func SummarizeHandler(c *gin.Context) {
	url := "https://resume-help.vercel.app/summarize"

	response, err := http.Get(url)
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to make request"})
        return
    }
    defer response.Body.Close()

	body, err := ioutil.ReadAll(response.Body)
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to read response"})
        return
    }

    c.Data(response.StatusCode, response.Header.Get("Content-Type"), body)
}