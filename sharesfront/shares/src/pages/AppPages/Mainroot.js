import React from "react";
import { Outlet } from "react-router-dom";
import MainNavigation from "../../components/BaseComponents/Mainnavigation";

function MainRoot(){
    return(
        <React.Fragment>
            <MainNavigation/>
            <Outlet/>
        </React.Fragment>
    )
}

export default MainRoot