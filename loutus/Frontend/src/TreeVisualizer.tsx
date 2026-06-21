import { useState } from "react";

type TreeProps = {
  tree: any;
};

function TreeVisualizer({ tree }: TreeProps) {

  const [showInfo, setShowInfo] = useState(false);

  // Leaf node
  if ("prediction" in tree) {

    let color = "";

    switch (tree.prediction) {
      case "Healthy":
        color = "#4CAF50";
        break;

      case "Risk of burnout":
        color = "#FFD700";
        break;

      case "Vacation required":
        color = "#FF9800";
        break;

      case "Critical condition":
        color = "#F44336";
        break;

      default:
        color = "#2196F3";
    }

    return (
      <div
        onMouseEnter={() => setShowInfo(true)}
        onMouseLeave={() => setShowInfo(false)}
        style={{
          position: "relative",
          border: `3px solid ${color}`,
          backgroundColor: color,
          color: "white",
          borderRadius: "15px",
          padding: "10px",
          marginTop: "10px",
          width: "fit-content",
          fontWeight: "bold"
        }}
      >
        {tree.prediction}

        {showInfo && (
          <div
            style={{
              position: "absolute",
              top: "-35px",
              left: "0px",
              backgroundColor: "black",
              color: "white",
              padding: "5px",
              borderRadius: "5px",
              fontSize: "12px"
            }}
          >
            Records: {tree.count}
          </div>
        )}
      </div>
    );
  }

  return (
    <div style={{ marginLeft: "40px", marginTop: "20px" }}>

      {/* Current node */}
      <div
        onMouseEnter={() => setShowInfo(true)}
        onMouseLeave={() => setShowInfo(false)}
        style={{
          position: "relative",
          border: "2px solid black",
          backgroundColor: "#f2f2f2",
          borderRadius: "15px",
          padding: "10px",
          width: "fit-content",
          fontWeight: "bold"
        }}
      >
        {"threshold" in tree
          ? `${tree.feature} < ${tree.threshold}`
          : `${tree.feature} = ${tree.value}`}

        {showInfo && (
          <div
            style={{
              position: "absolute",
              top: "-35px",
              left: "0px",
              backgroundColor: "black",
              color: "white",
              padding: "5px",
              borderRadius: "5px",
              fontSize: "12px"
            }}
          >
            Records: {tree.count}
          </div>
        )}
      </div>

      {/* YES branch */}
      <div
        style={{
          marginLeft: "40px",
          marginTop: "15px",
          borderLeft: "3px solid green",
          paddingLeft: "15px"
        }}
      >
        <div
          style={{
            color: "green",
            fontWeight: "bold",
            marginBottom: "10px"
          }}
        >
          ├── YES
        </div>

        <TreeVisualizer tree={tree.left} />
      </div>

      {/* NO branch */}
      <div
        style={{
          marginLeft: "40px",
          marginTop: "15px",
          borderLeft: "3px solid red",
          paddingLeft: "15px"
        }}
      >
        <div
          style={{
            color: "red",
            fontWeight: "bold",
            marginBottom: "10px"
          }}
        >
          └── NO
        </div>

        <TreeVisualizer tree={tree.right} />
      </div>

    </div>
  );
}

export default TreeVisualizer;