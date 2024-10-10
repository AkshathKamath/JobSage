package main

import (
	"backendv3/internal/aws"
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

//---------------------------------------------------------------------------//

func (app *application) Home(w http.ResponseWriter, r *http.Request) {

	var payload = struct {
		Status  string `json:"status"`
		Message string `json:"message"`
		Version string `json:"version"`
		Domain  string `json:"domain"`
	}{
		Status:  "Active",
		Message: "Up and running!",
		Version: "1.0.0",
		Domain:  app.Domain,
	}

	out, err := json.Marshal(payload)
	if err != nil {
		fmt.Println(err)
		return
	}

	w.Header().Set("Content-type", "application/json")
	w.WriteHeader(http.StatusOK)
	w.Write(out)
}

//---------------------------------------------------------------------------//

func (app *application) View(w http.ResponseWriter, r *http.Request) {
	url := "https://resume-help.vercel.app/view"

	response, err := http.Get(url)
	if err != nil {
		fmt.Fprint(w, "There was an error!")
		return
	}
	defer response.Body.Close()

	body, err := io.ReadAll(response.Body)
	if err != nil {
		fmt.Fprint(w, "There was an error!")
		return
	}

	w.Header().Set("Content-type", "application/json")
	w.WriteHeader(http.StatusOK)
	w.Write(body)
}

//---------------------------------------------------------------------------//

func (app *application) Summarize(w http.ResponseWriter, r *http.Request) {
	url := "https://resume-help.vercel.app/summarize"

	// type summary struct {
	// 	Summary string `json:"summary"`
	// }
	// payload := summary{}

	response, err := http.Get(url)
	if err != nil {
		fmt.Fprint(w, "There was an error!")
		return
	}
	defer response.Body.Close()

	body, err := io.ReadAll(response.Body)
	if err != nil {
		fmt.Fprint(w, "There was an error!")
		return
	}

	// err = json.Unmarshal(body, &payload)
	// if err != nil {
	// 	fmt.Fprint(w, "There was an error!")
	// }
	// out, err := json.Marshal(payload)
	// if err != nil {
	// 	fmt.Println(err)
	// }
	w.Header().Set("Content-type", "application/json")
	w.WriteHeader(http.StatusOK)
	w.Write(body)
}

//---------------------------------------------------------------------------//

func (app *application) Score(w http.ResponseWriter, r *http.Request) {
	url := "https://resume-help.vercel.app/score"

	body, err := io.ReadAll(r.Body)
	if err != nil {
		fmt.Fprint(w, "There was an error!")
		return
	}

	response, err := http.Post(url, "application/json", bytes.NewBuffer(body))
	if err != nil {
		fmt.Fprint(w, "There was an error!")
		return
	}
	defer response.Body.Close()

	body, err = io.ReadAll(response.Body)
	if err != nil {
		fmt.Fprint(w, "There was an error!")
		return
	}

	w.Header().Set("Content-type", "application/json")
	w.WriteHeader(http.StatusOK)
	w.Write(body)
}

//---------------------------------------------------------------------------//

func (app *application) S3Upload(w http.ResponseWriter, r *http.Request) {
	aws.FileUpload(r)
	fmt.Fprint(w, "File Uploaded")
}

//---------------------------------------------------------------------------//
