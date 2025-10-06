import React from "react";
import "./Search.css";

class Search extends React.Component {
  state = {
    search: "",
    type: "all",
    page: 1,
  };

  handleKey = (event) => {
    if (event.key === "Enter") {
      this.props.searchMovie(
        this.state.search,
        this.state.type,
        this.state.page
      );
    }
  };

  handelFilter = (event) => {
    this.setState(
      () => ({ type: event.target.dataset.type }),
      () => {
        this.props.searchMovie(
          this.state.search,
          this.state.type,
          this.state.page
        );
      }
    );
  };

  prevPage = () => {
    this.setState(
      this.state.page > 1 ? { page: this.state.page - 1 } : { page: 1 },
      () => {
        this.props.searchMovie(
          this.state.search,
          this.state.type,
          this.state.page
        );
      }
    );
  };

  nextPage = () => {
    this.setState({ page: this.state.page + 1 }, () => {
      this.props.searchMovie(
        this.state.search,
        this.state.type,
        this.state.page
      );
    });
  };

  render() {
    return (
      <>
        <div className="search">
          <input
            type="search"
            placeholder="Search"
            value={this.state.search}
            onChange={(e) => this.setState({ search: e.target.value })}
            onKeyDown={this.handleKey}
          />
          <button
            className="btn"
            onClick={() =>
              this.props.searchMovie(
                this.state.search,
                this.state.type,
                this.state.page
              )
            }
          >
            Search
          </button>
        </div>
        <div className="radio">
          <input
            type="radio"
            name="type"
            data-type="all"
            checked={this.state.type === "all"}
            onChange={this.handelFilter}
            id="all"
          />
          <label htmlFor="all">All</label>
          <input
            type="radio"
            name="type"
            data-type="movie"
            checked={this.state.type === "movie"}
            onChange={this.handelFilter}
            id="movies"
          />
          <label htmlFor="movies">Movies</label>
          <input
            type="radio"
            name="type"
            data-type="series"
            checked={this.state.type === "series"}
            onChange={this.handelFilter}
            id="series"
          />
          <label htmlFor="series">Series</label>
          <input
            type="radio"
            name="type"
            data-type="game"
            checked={this.state.type === "game"}
            onChange={this.handelFilter}
            id="games"
          />
          <label htmlFor="games">Games</label>
        </div>
        <div className="navigation">
          <button className="btn" onClick={this.prevPage}>
            Prev
          </button>
          <button className="btn" onClick={this.nextPage}>
            Next
          </button>
        </div>
      </>
    );
  }
}

export default Search;
