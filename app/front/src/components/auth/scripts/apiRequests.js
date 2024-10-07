async function hashUrlWithApiKey(url, apiKey) {
    const combinedString = url + apiKey;
    const encoder = new TextEncoder();
    const data = encoder.encode(combinedString);
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    return hashHex;
}

async function login(user, password, loginUrl, apiKey) {
	
	const data = { user, password };
	console.log('Login body:', data);
		
	const hashCalculated = await hashUrlWithApiKey(loginUrl, apiKey);
		
	const response = await fetch(loginUrl, {
		method: 'POST',
		headers: {
			'X-ApiKey': apiKey,
			'X-Hash': hashCalculated,
			'Content-Type': 'application/json'
		},
		mode: 'cors',
		body: JSON.stringify(data)
	})
	
	if (!response.ok) {
        const errorData = await response.json();
        throw new Error(JSON.stringify(errorData));
    }
    
    return response.json();
}

async function register(newUser, password, registerUrl, apiKey){

	const data = { newUser, password };
	const hashCalculated = await hashUrlWithApiKey(registerUrl, apiKey);
		
	const response = await fetch(loginUrl, {
		method: 'POST',
		headers: {
			'X-ApiKey': apiKey,
			'X-Hash': hashCalculated,
			'Content-Type': 'application/json'
		},
		mode: 'cors',
		body: JSON.stringify(data)
	})
	
	if (!response.ok) {
        const errorData = await response.json();
        throw new Error(JSON.stringify(errorData));
    }
    
    return response.json();
}
