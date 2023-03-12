import React from "react"
import { NavLink, useRouteLoaderData, Form } from "react-router-dom"


function MainNavigation(){
    const token = useRouteLoaderData("root")

    return(
        <React.Fragment>
            <header>
                <nav>
                    <ul>
                        {!token && (
                        <li>
                            <NavLink to="/">Welcome</NavLink>
                        </li>
                        )}
                        {token && (
                        <li>
                            <NavLink to="/index">Home Page</NavLink>
                        </li>
                        )}
                        {!token && (
                        <li>
                            <NavLink to="/auth?mode=login">Sign In</NavLink>
                        </li>
                        )}
                        {token && (
                        <Form action="logout" method="post">
                            <button>Logout</button>
                        </Form>
                         )}
                    </ul>
                </nav>
            </header>
        </React.Fragment>
    )
}

export default MainNavigation