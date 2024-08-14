import React from "react";
import "../App.css";
import { Container } from "react-bootstrap";
import NavbarComponent from "../components/Navbar";
import FeaturesComponent from "../components/Features";
import FileUploadComponent from "../components/FileUpload";

const HomePage = () => {
  return (
    <div>
      <NavbarComponent />
      <div className="mx-4 my-4">
        <Container align="center">
          <h3>Enhance your Resume with AI!</h3>
        </Container>
        <div className="my-4">
          <FeaturesComponent />
        </div>
        <div className="my-4">
          <FileUploadComponent />
        </div>
      </div>
    </div>
  );
};

export default HomePage;
