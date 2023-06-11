import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from 'react-responsive-carousel';

const DemoCarousel = ()=> {
        return (
            <Carousel showArrows={true}  >
                <div>
                    <img src="X.webp" alt='' />
                    <p className="legend">Legend 1</p>
                </div>
                <div>
                    <img src="M.webp" alt='' />
                    <p className="legend">Legend 2</p>
                </div>
                <div>
                    <img src="images\H.jpg
" alt='' />
                    <p className="legend">Legend 3</p>
                </div>
                <div>
                    <img src="J.webp" alt='' />
                    <p className="legend">Legend 4</p>
                </div>
                <div>
                    <img src="M.webp" alt='' />
                    <p className="legend">Legend 5</p>
                </div>
                <div>
                    <img src="images\H.jpg" alt='' />
                    <p className="legend">Legend 6</p>
                </div>
            </Carousel>
        );
};

export default DemoCarousel
// Don't forget to include the css in your page 
// <link rel="stylesheet" href="carousel.css"/>
// Begin DemoSliderControls