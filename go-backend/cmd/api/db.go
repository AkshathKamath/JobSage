package main

import (
	"context"
	"log"

	"github.com/jackc/pgx/v4"
)

//---------------------------------------------------------------------------//

func (app *application) ConnectDB() *pgx.Conn {
	databaseURL := app.DbURL

	//Connect database
	conn, err := pgx.Connect(context.Background(), databaseURL)
	if err != nil {
		log.Fatalf("Unable to connect to database: %v", err)
		return nil
	}
	log.Println("Database connected")
	return conn
}

//---------------------------------------------------------------------------//
