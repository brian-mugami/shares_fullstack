import React from "react";

function ShareList({shares}){
    return(
        <React.Fragment>
            <table>
                <thead>
                    <tr>
                    <th> company</th>
                    <th> ticker</th>
                    <th> volume</th>
                    <th> current price</th>
                    <th> last price</th>
                    <th> change</th>
                    <th> industry</th>
                    <th> last updated</th>
                    </tr>
                </thead>
                <tbody>
                    {shares.map((share) => (
                        <tr key={share.id}>
                            <td>{share.company}</td>
                            <td>{share.ticker}</td>
                            <td>{share.volume}</td>
                            <td>{share.current_price}</td>
                            <td>{share.last_price}</td>
                            <td>{share.change}</td>
                            <td>{share.industry}</td>
                            <td>{share.last_updated}</td>
                        </tr>))}
                </tbody>
            </table>
        </React.Fragment>
    )
}

export default ShareList;