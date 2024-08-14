package routes

import (
    "github.com/gin-gonic/gin"
    "resumesage/handlers"
)

func SetupRoutes(router *gin.Engine) {
    //Setting up routes
    router.GET("/", handlers.HomeHandler)
    router.GET("/summarize", handlers.SummarizeHandler)
    router.POST("/score", handlers.ScoreHandler)
    router.POST("/upload", handlers.S3UploadHandler)
}