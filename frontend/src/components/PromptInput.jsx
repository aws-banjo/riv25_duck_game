import React from 'react'

/**
 * PromptInput Component
 * 
 * A simple input field for duck descriptions.
 * This component is COMPLETE and working.
 */
function PromptInput({ value, onChange, onSubmit, disabled }) {
  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !disabled) {
      onSubmit()
    }
  }

  return (
    <div className="input-section">
      <label htmlFor="duck-prompt">
        Describe your duck:
      </label>
      <input
        id="duck-prompt"
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onKeyPress={handleKeyPress}
        placeholder="e.g., a duck wearing sunglasses on a beach"
        disabled={disabled}
      />
    </div>
  )
}

export default PromptInput
