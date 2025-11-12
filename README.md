# 🦆 Duck Generator Challenge

## What You're Building

An AI-powered duck image generator! Describe any duck you can imagine, and AWS Bedrock Nova Canvas will create it.

**Examples:**
- "a duck wearing sunglasses on a beach"
- "a cyberpunk duck with neon lights"  
- "a duck in a spacesuit floating in space"
- "a duck wearing a crown on a throne"

## What's Already Setup

✅ **Backend:** Strands agent with Nova Canvas - already deployed  
✅ **Frontend:** React app - has bugs you'll fix  
✅ **AWS Account:** Bedrock access configured  
✅ **6 MCP Servers:** Pre-configured tools Kiro can use:
- Nova Canvas (image generation)
- AWS Docs (documentation lookup)
- Frontend MCP (component analysis)
- Code Doc Gen (auto-documentation)
- Strands Agents (agent tools)
- Chrome DevTools (browser automation)

**You just need to fix 4 things!**

---

## Your 4 Tasks (~25 minutes)

### Task 1: Start Backend & Test MCP (5 min)

First, let's start the duck generator backend and test it works!

**Start the backend:**
```bash
cd backend
python duck_agent.py
```

Keep this terminal running. Open a new terminal for the next steps.

**Ask Kiro:**
```
"What MCP servers are available?"
```

**Test the backend with Nova Canvas:**
```
"Use Nova Canvas MCP to generate a test duck image and show me the result"
```

✅ **Success:** Backend is running, MCP servers work, you got a duck image!

---

### Task 2: Create Coding Standards (5 min)

Tell Kiro how you want code written using a "steering doc".

**Ask Kiro:**
```
"Create a steering doc at .kiro/steering/duck-standards.md with these rules:
- All API functions use duck-themed names (quackFetch, waddle, etc.)
- Prompts must include 'duck'
- Error messages are encouraging and duck-themed
- Use async/await for API calls"
```

✅ **Success:** Kiro now follows your duck-themed conventions!

---

### Task 3: Build the Duck Generator (10 min)

The app is broken. Write a "spec" describing what you want, then let Kiro build it!

**Create:** `specs/duck-generator-feature.md`

**Describe what you want:**
- Input field for duck description
- "Generate Duck" button
- Loading state ("Hatching your duck...")
- Display the generated duck image
- "Generate Another" button
- Handle errors with duck puns

**Ask Kiro:**
```
"Implement the duck generator from my spec"
```

✅ **Success:** Working duck generator! 🦆

---

### Task 4: Test with Chrome DevTools (5 min) 🎉

Watch Kiro test your app automatically in a real browser!

**Start the app:**
```bash
cd frontend
npm run dev
```

**Ask Kiro:**
```
"Use Chrome DevTools MCP to open localhost:5173 and test my duck generator"
```

**Watch the magic:** Kiro opens Chrome, tests your app, and takes a screenshot!

✅ **Success:** THE WOW MOMENT! 🚀

---

## Quick Tips

💬 **Talk to Kiro naturally** - "Can you help me with this?"  
🐛 **Stuck?** Ask Kiro to explain or fix bugs  
🎨 **Be creative** with your duck descriptions!  
📚 **Want to learn more?** https://kiro.dev/docs/

---

## You're Done When...

✅ You can describe a duck and see it generated  
✅ Kiro tested your app in Chrome automatically  
✅ You have a screenshot of your custom duck!

**Now generate your dream duck and take it home!** 🦆✨
