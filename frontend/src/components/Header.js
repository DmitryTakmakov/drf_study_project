import React from "react";

const HeaderItem = ({apiName}) => {
  return (
    <li className="nav-item">
      <a className="nav-link" aria-current="page" href="#">
        {apiName}
      </a>
    </li>
  )
};

const HeaderMenu = ({apis}) => {
  return (
    <nav className="navbar sticky-top navbar-expand-lg navbar-light bg-light">
      <div className="container-fluid">
        <span className="navbar-brand">Available APIs</span>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            {apis.map((apiName) => <HeaderItem apiName={apiName}/>)}
          </ul>
        </div>
      </div>
    </nav>
  )
};

export default HeaderMenu;