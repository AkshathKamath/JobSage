import React, { useState } from "react";
import { Button, Container } from "react-bootstrap";
import NavbarComponent from "../components/Navbar";
import PdfViewerModal from "../components/PdfModal";

const ViewPage = () => {
  const [modalShow, setModalShow] = useState(true);
  const pdfUrl = "https://resumehelp.s3.amazonaws.com/Resume.pdf";

  return (
    <div>
      <NavbarComponent />
      <Container className="mt-5">
        <Button variant="secondary" onClick={() => setModalShow(true)}>
          View Resume
        </Button>

        <PdfViewerModal
          show={modalShow}
          onHide={() => setModalShow(false)}
          pdfUrl={pdfUrl}
        />
      </Container>
    </div>
  );
};

export default ViewPage;
