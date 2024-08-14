import React from "react";
import { Navbar, NavbarBrand } from "react-bootstrap";
import "../App.css";

const NavbarComponent = () => {
  return (
    <Navbar bg="dark" variant="dark">
      <NavbarBrand href="/" className="mx-4">
        <img src="./ResumeSage_logo.png" className="logo mx-2"></img>
        ResumeSage
      </NavbarBrand>
      <NavbarBrand href="/summarize" className="fs-6 mx-10">
        Summarize
      </NavbarBrand>
      <NavbarBrand href="/score" className="fs-6">
        JD-Score
      </NavbarBrand>
    </Navbar>
  );
};

export default NavbarComponent;
