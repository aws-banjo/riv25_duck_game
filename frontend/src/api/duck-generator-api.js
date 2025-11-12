/**
 * Duck Generator API Client
 * 
 * ⚠️ THIS FILE HAS BUGS! ⚠️
 * 
 * Issues to fix:
 * 1. Function names are not duck-themed (violates steering doc conventions)
 * 2. Missing error handling
 * 3. Has a typo in the endpoint URL
 * 4. console.log statements left in (should be removed)
 */

const API_BASE_URL = import.meta.env.VITE_AGENT_ENDPOINT || 'http://localhost:8081'

/**
 * Generate a duck image based on description
 * 
 * TODO: Rename this to use duck-themed naming (e.g., quackFetch, generateDuck, etc.)
 */
export async function fetchDuckImage(description) {
    console.log('Generating duck:', description) // TODO: Remove console.log

    // BUG: Typo in endpoint - should be /api/duck/generate
    const response = await fetch(`${API_BASE_URL}/api/duk/generate`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ description }),
    })

    // BUG: No error handling!
    const data = await response.json()

    console.log('Duck generated:', data) // TODO: Remove console.log

    return data
}

/**
 * Check if the API is healthy
 * 
 * TODO: Rename to use duck-themed naming
 */
export async function checkHealth() {
    // BUG: No error handling!
    const response = await fetch(`${API_BASE_URL}/health`)
    const data = await response.json()
    return data
}
