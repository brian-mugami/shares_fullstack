import React from 'react'

function PageContent({title, children}){
    return(
        <React.Fragment>    
            <div>
                <h1>{title}</h1>
                {children}
            </div>
        </React.Fragment>
    )
}

export default PageContent;