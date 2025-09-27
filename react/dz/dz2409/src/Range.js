import React from "react";

class Range extends React.Component {
  state = { val: 100 };

  range = (event) => {
    this.setState({ val: event.target.value });
  };

  render() {
    return (
      <>
        <input
          type="range"
          onInput={this.range}
          min="60"
          max="240"
          step="20"
          style={{ accentColor: "blue" }}
        />
        <p>
          {this.state.val}px x {this.state.val}px
        </p>
        <div
          style={{
            border: "2px solid black",
            background: "blue",
            width: this.state.val + "px",
            height: this.state.val + "px",
            margin: "0 auto",
            display: "block"
          }}
        ></div>
      </>
    );
  }
}

export default Range;
