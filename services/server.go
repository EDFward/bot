package main

import (
	"fmt"
	"net/http"
	"os"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World")
}

func main() {
	http.HandleFunc("/", handler)

    hostport := fmt.Sprintf("%s:%s", os.Getenv("IP"), os.Getenv("PORT"))
	http.ListenAndServe(hostport, nil)
}
