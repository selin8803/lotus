import { useState, useEffect } from "react";
import TreeVisualizer from "./TreeVisualizer";

function App() {

  const [sleep, setSleep] = useState(8);
  const [meetings, setMeetings] = useState(2);
  const [stress, setStress] = useState(3);
  const [weekends, setWeekends] = useState(false);
  const [prediction, setPrediction] = useState("");
  const [tree, setTree] = useState<any>(null);

  useEffect(() => {

    fetch("http://localhost:5000/api/tree")
      .then(response => response.json())
      .then(data => setTree(data));

  }, []);

  const handlePredict = async () => {

    try {

      const response = await fetch("http://localhost:5000/api/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          sleep: sleep,
          Meetings: meetings,
          Stress: stress,
          Weekends: weekends ? "Yes" : "No"
        })
      });

      const data = await response.json();

      setPrediction(data.prediction);

    }
    catch (error) {

      console.error(error);

    }
  };

  return (
    <div>

      <h1>Burnout Analysis Dashboard</h1>

      <h3>Sleep: {sleep}</h3>
      <input
        type="range"
        min="1"
        max="12"
        value={sleep}
        onChange={(e) => setSleep(Number(e.target.value))}
      />

      <h3>Meetings: {meetings}</h3>
      <input
        type="range"
        min="0"
        max="10"
        value={meetings}
        onChange={(e) => setMeetings(Number(e.target.value))}
      />

      <h3>Stress: {stress}</h3>
      <input
        type="range"
        min="1"
        max="10"
        value={stress}
        onChange={(e) => setStress(Number(e.target.value))}
      />

      <h3>Work on weekends</h3>

      <input
        type="checkbox"
        checked={weekends}
        onChange={(e) => setWeekends(e.target.checked)}
      />

      <br />
      <br />

      <button onClick={handlePredict}>
        Predict
      </button>

      <h2>
        Prediction: {prediction}
      </h2>

      <hr />

      <h1>Decision Tree</h1>
      <h2>{tree ? "Tree loaded" : "Tree not loaded"}</h2>
      {tree && <TreeVisualizer tree={tree} />}

    </div>
  );
}

export default App;