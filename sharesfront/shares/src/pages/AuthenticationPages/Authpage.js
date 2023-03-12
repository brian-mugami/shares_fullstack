import { json, redirect } from "react-router-dom";
import AuthForm from "../../components/AuthComponents/AuthForm";

function AuthPage(){
    return(
        <AuthForm/>
    )
}

export default AuthPage

export async function action ({request}){
    const searchParams = new URL(request.url).searchParams
    const mode = searchParams.get('mode') || 'login'

    if (
        mode !== 'login' && mode !== 'register'
      ){
        throw json({message: "Route not found."}, {status:404})
      }
    const data = await request.formData()

    const regData = {
    date_of_birth: data.get('birth'),
    email: data.get('email'),
    password: data.get('password1'),
    password2: data.get('password2'),
    }

    const loginData = {
    email: data.get('email'),
    password: data.get('password'),        
    }

    if (mode==='login'){
        const response = await fetch('http://localhost:8080/api/user/login', {
            method: "POST",
            headers: {
                'Content-Type':'application/json',
            },
            body: JSON.stringify(loginData)
        })
        if (!response){
            throw json ({message:"Could not authenticate user"}, {status: 500})
          }
          if(response.status === 401){
            throw json({message:"Unauthorized"},{status:401})
          }

          const resData = await response.json();
          const access_token = resData.access;
          const refresh_token = resData.refresh;
        
          localStorage.setItem('access_token', access_token)
          localStorage.setItem('refresh_token', refresh_token)
          const expiration = new Date()
          expiration.setHours(expiration.getHours() + 36)
          localStorage.setItem('expiration', expiration.toISOString())
        
          // manage tokens
          return redirect("/index")}
        
    if(mode==='register'){
        const response = await fetch('http://localhost:8080/api/user/register', {
            method: "POST",
            headers: {
                'Content-Type':'application/json',
            },
            body: JSON.stringify(regData)
        })
        if(response.status === 404){
            return response
          } 
        
        if (response.status === 401){
          throw json({message:"You are not authorized to"}, {status: 401})
        }  

        if(response.status === 417){
            return response
          } 
        if (!response.ok){
            throw json ({message:"Could not register user"}, {status: 500})
          }

          return redirect("/login")
    }
}
