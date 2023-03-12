import PageContent from "../../components/BaseComponents/PageContent"
import MainNavigation from "../../components/BaseComponents/Mainnavigation"
import React from "react"
import { useRouteError } from "react-router-dom"

function ErrorPage(){
    const error = useRouteError()

    let title ="error page"
    let message = "this is the main error"

    if (error.status === 404) {
        title = "404 page"
        message = "this is the 404 page"
    }
    if (error.status === 500) {
        title = "Server error"
        message = "this is the 500 page"
    }
    if (error.status === 401) {
        title = "Unauthorized"
        message = "Please login"
    }

    return(
        <React.Fragment>
            <MainNavigation/>
            <PageContent title={title}>
                <p>{message}</p>
            </PageContent>
        </React.Fragment>
    )
}

export default ErrorPage