import QuotesDatabase from './QuotesDatabase'
import React from 'react'
import Helmet from "react-helmet"

class Quotes extends React.Component {
    constructor() {
        super();
        this.state = {
            quote: QuotesDatabase[1].quote,
            author: QuotesDatabase[1].author,
            key: 1,
            color: 'ee350d',
            colors: ['ee170d', 'fc4e03', 'fcc703', 'edfc03', '65fc03', '38fc03', '03fc1a', '03fc8f', '03fced', '0307fc', '7003fc', 'f803fc', 'fc0347', '3b3636', 'f1727a']    
        }
    }

handleChange = (e) => {
  let randomIndexQuote;
  let randomIndexColor;

  do {
    randomIndexQuote = Math.floor(Math.random() * QuotesDatabase.length);
  } while (randomIndexQuote === this.state.quoteIndex);

  do {
    randomIndexColor = Math.floor(Math.random() * this.state.colors.length);
  } while (randomIndexColor === this.state.colorIndex);

    console.log("quote and author", QuotesDatabase[randomIndexQuote].quote, QuotesDatabase[randomIndexQuote].author);
    this.setState((prevState) => ({
      quote: QuotesDatabase[randomIndexQuote].quote,
      author: QuotesDatabase[randomIndexQuote].author,
      color: this.state.colors[randomIndexColor],
      key: prevState.key + 1
    }));

}


render () {

    return(

      <div key={this.state.key}>
          <Helmet>
            <style>{`body { background-color: #${this.state.color}; }`}</style>
          </Helmet>
          <div className="textall" style={{ backgroundColor: 'white' }}>
            <style>
              {`
                @keyframes fallAnimation {
                  from {
                    opacity: 0;
                    transform: translateY(-20px);
                  }
                  to {
                    opacity: 1;
                    transform: translateY(0);
                  }
                }
  
                .quoteauthor, .change {
                  animation: fallAnimation 0.9s ease forwards;
                }
              `}
            </style>
            <div className="quoteauthor">
              <h2 style={{ color: '#' + this.state.color }}>{this.state.quote}</h2>
              <p style={{ color: '#' + this.state.color }}>{this.state.author}</p>
            </div>
        <button className="change" onClick={this.handleChange} style={{ backgroundColor: "#"+this.state.color }}> New quote
        </button>
      </div>
        </div>
        )}
}

export default Quotes
        