import React, { Suspense } from "react";
import { Await, defer, json, useLoaderData } from "react-router-dom";
import ShareList from "../../components/AppComponents/ShareList";
import { getAuthToken } from "../../utils/utils";


function IndexPage(){
    const {shares} = useLoaderData();
    return(
            <Suspense fallback={<p style={{ textAlign: 'center' }}>Loading...</p>}>
                <Await resolve={shares}>
                    {(loadedShares) => <ShareList shares={loadedShares} />}
                </Await>
            </Suspense>
    )
}

export default IndexPage;

async function sharesListLoader(){
    const token = getAuthToken()

    const response = await fetch("http://localhost:8080/api/share", {
        method: "GET",
        headers:{
            "Authorization": "Bearer " + token
        }
    });

    if (!response.ok){
        throw json({message: "Failed to fetch shares"}, {status: 500})
    }

    const data = await response.json();
    console.log(data);
    return data;
}

export function loader(){
    return(
        defer({
            shares: sharesListLoader(),
        })
    )
}
