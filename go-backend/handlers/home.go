package handlers

import (
    "github.com/gin-gonic/gin"
    "net/http"
)

func HomeHandler(c *gin.Context) {
    c.JSON(http.StatusOK, gin.H{"msg": "Hello, World!"})
}