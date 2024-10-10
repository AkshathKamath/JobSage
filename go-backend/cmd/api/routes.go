package main

import (
	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
)

func (app *application) routes() http.Handler {
	mux := chi.NewRouter() //Create router

	mux.Use(middleware.Recoverer)
	mux.Use(app.enableCORS)

	mux.Get("/", app.Home)
	mux.Get("/view", app.View)
	mux.Get("/summarize", app.Summarize)
	mux.Post("/score", app.Score)
	mux.Post("/upload", app.S3Upload)

	return mux
}
