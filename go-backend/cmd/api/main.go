package main

import (
	"context"
	"fmt"
	"log"
	"net/http"

	"github.com/jackc/pgx/v4"
)

const port = 8000

type application struct {
	Domain       string
	DbURL        string
	DbConnection *pgx.Conn
}

func main() {
	//Defining App
	var app application
	app.Domain = "example.com"
	app.DbURL = "postgresql://postgres.tlzpxquqcaasetkdjmvo:Akshath251972@aws-0-us-east-1.pooler.supabase.com:6543/postgres"
	app.DbConnection = app.ConnectDB()

	defer app.DbConnection.Close(context.Background()) //Close the connection

	//Start server
	log.Println("Starting application on port", port)
	err := http.ListenAndServe(fmt.Sprintf(":%d", port), app.routes())
	if err != nil {
		log.Fatal(err)
	}
}
