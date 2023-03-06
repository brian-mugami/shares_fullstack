import PageContent from "../../components/BaseComponents/PageContent"
import MainNavigation from "../../components/BaseComponents/Mainnavigation"
import React from "react"

function ErrorPage(){
    let title ="error page"
    let message = "this is the main error"

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