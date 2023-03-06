import { createBrowserRouter, RouterProvider } from "react-router-dom"
import MainRoot from "./pages/AppPages/Mainroot";
import { tokenLoader } from "./utils/utils";
import ErrorPage from "./pages/AppPages/ErrorPage";
import Homepage from "./pages/AppPages/Home";
import AuthPage,{action as authaction}from "./pages/AuthenticationPages/Authpage";
import {action as logoutaction} from "./pages/AuthenticationPages/Logout"

const router = createBrowserRouter([
  {
    path:"/",
    element:<MainRoot/>,
    loader: tokenLoader,
    errorElement:<ErrorPage/>,
    id:"root",
    children:[
      {index: true, element:<Homepage/>},
      {path:"auth", element:<AuthPage/>, action: authaction},
      {path:"logout",action: logoutaction}
    ]
  }])

function App() {
  return (
      <RouterProvider router={router}></RouterProvider>
  );
}

export default App;
