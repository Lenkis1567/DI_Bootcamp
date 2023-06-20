import Superheroes from './Heroes.js'
import React from 'react'

class Heroapp extends React.Component {
    constructor() {
        super();
        const shuffledSuperheroes = Superheroes.sort(() => Math.random() - 0.5);
        this.state = {
            score: 0,
            maxscore:0,
            maxscores: [],
            superheroes: [...Superheroes],
            clickedheroes: [], 
            clickedSuperhero: null,
            
        }
    }

    handleCardClick = (index) => {
        const { superheroes, clickedSuperhero, clickedheroes, score, maxscore } = this.state;
        const clickedSuperheroNew = superheroes[index];
        console.log(clickedSuperheroNew);
      
        const isAlreadyClicked = clickedheroes.some(
          (hero) => hero.name === clickedSuperheroNew.name
        );
      
        if (isAlreadyClicked) {
          console.log('Hero already clicked!');
          if (score > this.state.maxscore && this.state.maxscores.every((max) => max < score)) {
            this.setState({ maxscore: score });
            this.setState({ maxscores: [...this.state.maxscores, score] });
          }
          this.setState({ score: 1, clickedheroes: [clickedSuperheroNew] });
        } else {
          const updatedClickedHeroes = [...clickedheroes, clickedSuperheroNew];
          this.setState({ clickedheroes: updatedClickedHeroes }, () => {
            console.log(this.state.clickedheroes);
            this.setState({ score: score + 1 });
          });
        }
      
        const updatedSuperheroes = [...superheroes];
        const clickedSuperheroIndex = updatedSuperheroes.findIndex(
          (hero) => hero === clickedSuperhero
          
        );
        updatedSuperheroes[clickedSuperheroIndex] = clickedSuperheroNew;
        const shuffledSuperheroes = updatedSuperheroes.sort(() => Math.random() - 0.5);
      
        this.setState({
          superheroes: [...shuffledSuperheroes],
          clickedSuperhero: clickedSuperheroNew,
        });
      };

    render () {
        const { superheroes } = this.state;
        return(
            <div className='main'>
                <header>
                    <div className='results'>
                        <h1>Superheroes Memory Game</h1>
                        <div className="score">
                            <p>Score:
                                <span>{this.state.score}</span>
                            </p>
                            <p>Top score:
                                <span>{this.state.maxscore}</span>
                            </p>
                        </div>
                    </div>
                </header>
                <div className='slogan'>
                    <p className='pslogan'>Get points by clicking on an image but don't click on any more than once!</p>
                </div>
                <div className='cardsall'>
                 {superheroes.map((superhero, index) => (
                    <div
                    className='card'
                    key={index}
                    onClick={() => this.handleCardClick(index)}
                    >
                        <div className='imgcard'>
                            <img src={superhero.image} alt={superhero.name} />
                        </div>
                        <div className='textcard'>
                            <ul>
                            <li><strong>Name: </strong>{superhero.name}</li>
                            <li><strong>Occupation: </strong>{superhero.occupation}</li>
                            </ul>
                        </div>
                        </div>
                    ))}
                    </div>

            </div>
        )
    }
}

export default Heroapp