import React from "react";
import { Form, Link, useSearchParams, useActionData, useNavigation } from "react-router-dom";

function AuthForm(){
    const data = useActionData()
    const [searchParams] = useSearchParams()
    const navigation = useNavigation()

    const isSubmitting = navigation.state === 'submitting'  
    const isLogin = searchParams.get('mode') === 'login'

    return(
        <React.Fragment>
            {!isLogin && 
                <Form method="post">
                     <h1>{isLogin ? 'Log in' : 'Register Here'}</h1>
                     {data && data.errors && <ul>
                    {Object.values(data.errors).map((err)=>(<li key={err}>{err}</li>))}</ul>}
                    {data && data.message && <p>{data.message}</p>}
                <p>
                    <label>Email</label>
                    <input id="email" type="email" name="email" required placeholder="Enter your Email" />
                </p>
                <p>
                    <label >Password</label>
                    <input id="password1" type="password" name="password1" required placeholder="Enter your password"/>
                </p>
                <p>
                    <label >Re-type Password</label>
                    <input id="password2" type="password" name="password2" required placeholder="Retype your password" />
                </p>
                <p>
                    <label >Date of Birth</label>
                    <input id="birth" type="date" name="birth" required placeholder="Enter your Date of birth"/>
                </p>
                    <button>
                    <Link to={`?mode=${isLogin ? 'register': 'login'}`}>
                        {isLogin? 'Register': 'Login'}
                    </Link>
                    </button>
                    <button disabled={isSubmitting}>{isSubmitting ? 'Registering...' : 'Register'}</button>
                
                </Form>
            }
            {isLogin && 
             <Form method="post">
                <h1>{isLogin ? 'Log in' : 'Create a new user'}</h1>
                {data && data.errors && <ul>
                {Object.values(data.message).map((err)=>(<li key={err}>{err}</li>))}</ul>}
                {data && data.message && <p>{data.message}</p>}
             <p>
                 <label>Email</label>
                 <input id="email" type="email" name="email" required placeholder="Enter your Email" />
             </p>
             <p>
                 <label >Password</label>
                 <input id="password" type="password" name="password" required placeholder="Enter your password"/>
             </p>
                <button>
                 <Link to={`?mode=${isLogin ? 'register': 'login'}`}>
                     {isLogin? 'Register': 'Login'}
                 </Link>
                 </button>
                 <button disabled={isSubmitting}>{isSubmitting ? 'Submitting...' : 'Submit'}</button>
             </Form>}

        </React.Fragment>
    )
}

export default AuthForm;