const Planets = (props) => {
  return (
    <div className="container">
      <div className="row">
        <div className="col d-flex justify-content-center">
          <ul className="list-group" style={{ Width: '400px' }}>
          {props.planets.map((planet, index) => (
            <li className="list-group-item" key={index} id={index}>
            {planet} </li>
      ))}
    </ul>
    </div>
    </div>
    </div>
  );
};

export default Planets;