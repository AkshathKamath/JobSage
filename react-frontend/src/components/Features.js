import React from "react";

const FeaturesComponent = () => {
  return (
    <div>
      <h5>Features</h5>
      <div className="list-group">
        <p className="list-group-item list-group-item-action flex-column align-items-start features">
          <div className="d-flex w-100 justify-content-between features">
            <b className="mb-1">Summarize your resume in seconds.</b>
          </div>
          <p className="mb-1">
            Generate a brief, two-line summary of your resume, highlighting
            yourmost relevant skills and experiences. This feature provides a
            quick snapshot for easy review. Use it directly as your LinkedIN
            bio!
          </p>
        </p>
        <p className="list-group-item list-group-item-action flex-column align-items-start features">
          <div className="d-flex w-100 justify-content-between features">
            <b className="mb-1">Create the Ideal resume for your dream Job.</b>
          </div>
          <p className="mb-1">
            Compare how well your resume fits with the Job description of your
            dream role. Generate a score that rates the resume-JD fit and also
            suggests improvements you can make that increases your chances of
            getting shortlisted!
          </p>
        </p>
        <p className="list-group-item list-group-item-action flex-column align-items-start features">
          <div className="d-flex w-100 justify-content-between features">
            <b className="mb-1">More Features coming soon!</b>
          </div>
        </p>
      </div>
    </div>
  );
};

export default FeaturesComponent;
