import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { ChakraProvider, VStack, Card, CardHeader, Heading, Textarea, Flex, HStack, Button} from '@chakra-ui/react'
import {Clipboard, FilePlus} from 'react-feather'

function App() {
  let [value, setValue] = useState('')

  

  return (
    <ChakraProvider>
      <Flex height="100vh" alignItems="center" justifyContent="center">
      <VStack spacing={20} align="stretch" width="80vw">
        <Card maxW="80vw" p={4}>
          
          <CardHeader>
            <HStack>
            <Heading size='md'>Enter Text to Summarize</Heading>
            <Button ml={5}><FilePlus/></Button>
            </HStack>
          </CardHeader>
          <Textarea
            value={value}
            onChange={(e) => setValue(e.target.value)}
            placeholder="Enter text to summarize here"
            size="sm"
           
          />
        </Card>
        <Card maxW="80vw" p={4}>
          <CardHeader>
          <HStack>
            <Heading size='md'>Summarized Text</Heading>
            <Button ml={5}><Clipboard/></Button>
            </HStack>
          </CardHeader>
          <Textarea
            value={value}
            isReadOnly
            placeholder="Summarized text will appear here"
            size="sm"
           
          />
        </Card>
      </VStack>
    </Flex>
    </ChakraProvider>
  )
}

export default App
