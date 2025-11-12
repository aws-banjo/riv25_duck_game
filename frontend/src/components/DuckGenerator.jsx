import React, { useState } from 'react'
import PromptInput from './PromptInput'
import { fetchDuckImage } from '../api/duck-generator-api'

/**
 * DuckGenerator Component
 * 
 * ⚠️ THIS COMPONENT IS INCOMPLETE! ⚠️
 * 
 * Missing features:
 * 1. State management for generated duck image
 * 2. Loading state while generating
 * 3. Error handling and display
 * 4. Image display component
 * 5. "Generate Another" button functionality
 * 
 * Participants should create a SPEC to define these requirements,
 * then ask Kiro to implement them!
 */
function DuckGenerator() {
  const [prompt, setPrompt] = useState('')
  // TODO: Add state for:
  // - loading (boolean)
  // - generatedDuck (object with image and message)
  // - error (string or null)

  const handleGenerate = async () => {
    // TODO: Implement this function!
    // Should:
    // 1. Validate prompt is not empty
    // 2. Set loading state
    // 3. Call fetchDuckImage API
    // 4. Handle success (store image)
    // 5. Handle errors (show error message)
    // 6. Clear loading state
    
    console.log('Generate button clicked with prompt:', prompt)
    // BUG: This doesn't actually do anything!
  }

  return (
    <div className="generator-container">
      <PromptInput
        value={prompt}
        onChange={setPrompt}
        onSubmit={handleGenerate}
        disabled={false} // TODO: Should be disabled while loading
      />
      
      <button 
        className="button-primary"
        onClick={handleGenerate}
        disabled={false} // TODO: Should be disabled while loading or if prompt is empty
      >
        Generate Duck
      </button>
      
      {/* TODO: Add loading state display */}
      {/* TODO: Add error display */}
      {/* TODO: Add generated duck image display */}
      {/* TODO: Add "Generate Another" button */}
    </div>
  )
}

export default DuckGenerator
