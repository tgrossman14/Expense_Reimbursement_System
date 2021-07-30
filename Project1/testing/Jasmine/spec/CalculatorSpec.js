// Describe function denotes a test suite (collection of tests)
// BDD testing framework. Behavior-Driven Development
// Functions tested at a high level. Even non-coders can understand.
describe('Calculator Tests', () => {
    //Set up and tear down test bed before and after hooks.
    let calculator;
    beforeEach(() => {
        // Set up test bed
        calculator = new Calculator()
    })

it('should properly add two numbers together', () => {
    // Expectations, not assertions
    expect(calculator.add(5, 5)).toEqual(10)
})

it('should properly subtract two numbers', () => {
    // Expectations, not assertions
    expect(calculator.subtract(5, 5)).toEqual(0)
})

})