import { redirect } from "react-router-dom";

export function action(){
    const response = fetch('http://localhost:8080/api/user/logout')

    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('expiration');

    return redirect("/")
}