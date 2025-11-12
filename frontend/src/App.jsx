import React from 'react'
import DuckGenerator from './components/DuckGenerator'

function App() {
  return (
    <div className="app">
      <header className="header">
        <h1>🦆 Duck Generator</h1>
        <p>Describe your dream duck and watch it come to life!</p>
      </header>
      
      <DuckGenerator />
      
      <div className="examples">
        <h3>Need inspiration? Try these:</h3>
        <ul>
          <li>a duck wearing sunglasses on a beach</li>
          <li>a cyberpunk duck with neon lights</li>
          <li>a duck in a spacesuit floating in space</li>
          <li>a duck wearing a crown sitting on a throne</li>
          <li>a duck detective with a magnifying glass</li>
        </ul>
      </div>
    </div>
  )
}

export default App
