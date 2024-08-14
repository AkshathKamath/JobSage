package main

import (
	"github.com/gin-gonic/gin"
	"resumesage/routes"
	"fmt"
	// "net/http"
	"log"
	"github.com/joho/godotenv"
	"github.com/gin-contrib/cors"
	// "time"
)

const port = 8000

func main() {
	gin.SetMode(gin.ReleaseMode)

	err := godotenv.Load()
    if err != nil {
        log.Fatal("Error loading .env file")
    }

	router := gin.Default()

	// router.Use(func(c *gin.Context) {
    //     // Set CORS headers to allow all origins
    //     c.Writer.Header().Set("Access-Control-Allow-Origin", "*")
    //     c.Writer.Header().Set("Access-Control-Allow-Credentials", "true")
    //     c.Writer.Header().Set("Access-Control-Allow-Headers", "Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization, accept, origin, Cache-Control, X-Requested-With")
    //     c.Writer.Header().Set("Access-Control-Allow-Methods", "POST, OPTIONS, GET, PUT")

    //     // Allow preflight OPTIONS request
    //     if c.Request.Method == "OPTIONS" {
    //         c.AbortWithStatus(204)
    //         return
    //     }

    //     c.Next()
    // })

	router.Use(cors.New(cors.Config{
        AllowOrigins: []string{"*"}, // Set allowed origins
        AllowMethods: []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
        AllowHeaders: []string{"Origin", "Content-Type", "Accept", "Authorization"},
    }))

	// router.Use(func(c *gin.Context) {
    //     origin := c.Request.Header.Get("Origin")
    //     allowedOrigin := "https://resume-sage-cyan.vercel.app"

    //     if origin == allowedOrigin {
    //         c.Writer.Header().Set("Access-Control-Allow-Origin", origin)
    //     } else {
    //         c.Writer.Header().Set("Access-Control-Allow-Origin", "null")
    //     }

    //     c.Writer.Header().Set("Access-Control-Allow-Credentials", "true")
    //     c.Writer.Header().Set("Access-Control-Allow-Headers", "Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization, accept, origin, Cache-Control, X-Requested-With")
    //     c.Writer.Header().Set("Access-Control-Allow-Methods", "POST, OPTIONS, GET, PUT")

    //     // Handle preflight OPTIONS requests
    //     if c.Request.Method == http.MethodOptions {
    //         c.AbortWithStatus(http.StatusNoContent)
    //         return
    //     }

    //     c.Next()
    // })

	routes.SetupRoutes(router)

	fmt.Println("Server starting!")
	router.Run(fmt.Sprintf(":%d", port))
}