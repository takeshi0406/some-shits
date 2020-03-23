package main

import (
	"net/http"
)

func main() { // メイン処理
	http.HandleFunc("/", HelloHandler) // ハンドラを登録 --- (*1)
	http.ListenAndServe(":8888", nil)  // サーバーを起動 --- (*2)
}

// HelloHandler サーバーの処理内容を記述 --- (*3)
func HelloHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hello, World!")) // --- (*4)
}
