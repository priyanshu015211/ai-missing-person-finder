import { useEffect, useState } from "react";

import { getApiHealth } from "./api/client.js";

export default function App() {
  const [apiState, setApiState] = useState({
    loading: true,
    online: false,
    message: "Checking backend connection...",
  });

  useEffect(() => {
    let isMounted = true;

    getApiHealth()
      .then(({ data }) => {
        if (isMounted) {
          setApiState({
            loading: false,
            online: true,
            message: `${data.service} · v${data.version}`,
          });
        }
      })
      .catch(() => {
        if (isMounted) {
          setApiState({
            loading: false,
            online: false,
            message:
              "Backend unavailable. Start the FastAPI server on port 8000.",
          });
        }
      });

    return () => {
      isMounted = false;
    };
  }, []);

  return (
    <main className="page-shell">
      <section className="status-card" aria-labelledby="page-title">
        <p className="eyebrow">PROJECT FOUNDATION · PHASE 1</p>
        <h1 id="page-title">AI Missing Person Finder</h1>
        <p className="intro">
          A case-management platform designed to support missing-person
          reunification through authorized reporting and coordinator review.
        </p>

        <div
          className={`connection-status ${apiState.online ? "online" : "offline"}`}
          role="status"
          aria-live="polite"
        >
          <span className="status-dot" aria-hidden="true" />
          <span>{apiState.message}</span>
        </div>

        <p className="notice">
          Potential matches will require authorized human verification. An AI
          similarity result is not proof of identity.
        </p>
      </section>
    </main>
  );
}
