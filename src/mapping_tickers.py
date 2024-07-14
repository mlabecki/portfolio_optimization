# Components of Dow Jones Industrial Average
djia_components = {
    'AAPL': 'Apple Inc.',
    'AMGN': 'Amgen Inc.',
    'AMZN': 'Amazon.com, Inc.',
    'AXP': 'American Express Company',
    'BA': 'The Boeing Company',
    'CAT': 'Caterpillar, Inc.',
    'CRM': 'Salesforce, Inc.',
    'CSCO': 'Cisco Systems, Inc.',
    'CVX': 'Chevron Corporation',
    'DIS': 'The Walt Disney Company',
    'DOW': 'Dow Inc.',
    'GS': 'The Goldman Sachs Group, Inc.',
    'HD': 'The Home Depot, Inc.',
    'HON': 'Honeywell International Inc.',
    'IBM': 'International Business Machines Corporation',
    'INTC': 'Intel Corporation',
    'JNJ': 'Johnson & Johnson',
    'JPM': 'JP Morgan Chase & Co.',
    'KO': 'The Coca-Cola Company',
    'MCD': 'McDonald\'s Corporation',
    'MMM': '3M Company',
    'MRK': 'Merck & Company, Inc.',
    'MSFT': 'Microsoft Corporation',
    'NKE': 'Nike, Inc.',
    'PG': 'The Procter & Gamble Company',
    'TRV': 'The Travelers Companies, Inc.',
    'UNH': 'UnitedHealth Group Incorporated',
    'V': 'Visa Inc.',
    'VZ': 'Verizon Communications Inc.',
    'WMT': 'Walmart Inc.'
}
# Nasdaq 100 Top 30 companies as of 2024-07-11
ndx_top30_components = {
    'TSLA':	'Tesla, Inc.',
    'AAPL':	'Apple Inc.',
    'META':	'Meta Platforms, Inc.',
    'SBUX':	'Starbucks Corporation',
    'ARM': 'Arm Holdings plc',
    'MRVL': 'Marvell Technology, Inc.',
    'MDLZ': 'Mondelez International, Inc.',
    'MCHP': 'Microchip Technology Incorporated',
    'BKR': 'Baker Hughes Company',
    'KDP': 'Keurig Dr Pepper Inc.',
    'AMAT':	'Applied Materials, Inc.',
    'TXN': 'Texas Instruments Incorporated',
    'FTNT': 'Fortinet, Inc.',
    'DDOG':	'Datadog, Inc.',
    'MRNA': 'Moderna, Inc.',
    'CSGP': 'CoStar Group, Inc.',
    'AZN': 'AstraZeneca PLC',
    'HON': 'Honeywell International Inc.',
    'DLTR':	'Dollar Tree, Inc.',
    'ILMN': 'Illumina, Inc.',
    'CEG': 'Constellation Energy Corporation',
    'AMGN': 'Amgen Inc.',
    'PCAR': 'PACCAR Inc',
    'MAR': 'Marriott International, Inc.',
    'ZS': 'Zscaler, Inc.',
    'CCEP':	'Coca-Cola Europacific Partners PLC',
    'INTU':	'Intuit Inc.',
    'CDW': 'CDW Corporation',
    'VRSK':	'Verisk Analytics, Inc.',
    'MELI': 'MercadoLibre, Inc.'
}


# YouTube Portfolio Optimization example by Ryan O'Connell
# https://www.youtube.com/watch?v=9GA2WlYFeBU
yt_example_tickers = {
    'SPY': 'SPDR S&P 500 ETF Trust',
    'BND': 'Vanguard Total Bond Market Index Fund',
    'GLD': 'SPDR Gold Shares',
    'QQQ': 'Invesco QQQ Trust',
    'VTI': 'Vanguard Total Stock Market Index Fund ETF Shares'
}
# Top 50 crypotocurrencies by market cap (current price x circulating amount)
# as of July 10th, 2024
crypto_tickers = {
    'BTC-USD': 'Bitcoin USD',
    'ETH-USD': 'Ethereum USD',
    'USDT-USD': 'Tether USD',
    'BNB-USD': 'BNB USD',
    'SOL-USD': 'Solana USD',
    'USDC-USD': 'USDC USD',
    'XRP-USD': 'XRP USD',
    'TON-USD': 'Tokamak Network USD',
    'DOGE-USD': 'Dogecoin USD',
    'ADA-USD': 'Cardano USD',
    'TRX-USD': 'TRON USD',
    'AVAX-USD': 'Avalanche USD',
    'SHIB-USD': 'Shiba Inu USD',
    'DOT-USD': 'Polkadot USD',
    'LINK-USD': 'Chainlink USD',
    'BCH-USD': 'Bitcoin Cash USD',
    'DAI-USD': 'Dai USD',
    'LEO-USD': 'UNUS SED LEO USD',
    'NEAR-USD': 'NEAR Protocol USD',
    'MATIC-USD': 'Polygon USD',
    'UNI7083-USD': 'Uniswap USD',  # NOTE: UNI-USD is UNICORN Token USD in Yahoo!Finance
    'LTC-USD': 'Litecoin USD',
    'KAS-USD': 'Kaspa USD',
    'PEPE24478-USD':  'Pepe USD',  # NOTE: PEPE-USD is PEPEGOLD, a different cryptocurrency launched in 2024
    'ICP-USD': 'Internet Computer USD',
    'ETC-USD': 'Ethereum Classic USD',
    'FET-USD': 'Artificial Superintelligence Alliance USD',
    'XMR-USD': 'Monero USD',
    'APT-USD': 'Apricot Finance USD',
    'XLM-USD': 'Stellar USD',
    'RNDR-USD': 'Render USD',
    'HBAR-USD': 'Hedera USD',
    'ATOM-USD': 'Cosmos USD',
    'CRO-USD': 'Cronos USD',
    'OKB-USD': 'OKB USD',
    'ARB11841-USD': 'Arbitrum USD',  # NOTE: ARB-USD is ARbit USD in Yahoo!Finance)
    'MNT27075-USD': 'Mantle USD',  # NOTE: MNT-USD is microNFT USD in Yahoo!Finance
    'MKR-USD': 'Maker USD',
    'STX4847-USD': 'Stacks USD',  # NOTE: STX-USD is stox USD in Yahoo!Finance
    'FDUSD-USD': 'First Digital USD USD',
    'VET-USD': 'VeChain USD',
    'IMX10603-USD': 'Immutable USD',  # NOTE: IMX-USD is Impermax USD in Yahoo!Finance
    'INJ-USD': 'Injective USD',
    'SUI20947-USD': 'Sui USD',  # NOTE: SUI-USD is Salmonation USD in Yahoo!Finance
    'WIF-USD': 'dogwifhat USD',
    'GRT6719-USD': 'The Graph USD',  # NOTE: GRT-USD is Golden Ratio Token USD in Yahoo!Finance)
    'NOT-USD': 'Notcoin USD',
    'TAO22974-USD':'TaoPad USD (part of Bittensor network)',
    'OP-USD': 'Optimism USD'
}

