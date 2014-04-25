// hedgehog project main.go
package main

import (
	"net/http"
)

func main() {

	// main page
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		http.ServeFile(w, r, "./templates/hedgehog.html")
	})

	// static resources
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("./static/"))))

	http.ListenAndServe(":9090", nil)
}
