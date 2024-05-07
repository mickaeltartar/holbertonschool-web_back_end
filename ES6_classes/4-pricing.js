import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    if (!(currency instanceof Currency)) {
      throw new TypeError('Currency must be a currency');
    }
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(newamount) {
    if (typeof newamount !== 'number') {
      throw new TypeError('Amount must be a number');
    } else {
      this._amount = newamount;
    }
  }

  get currency() {
    return this._currency;
  }

  set currency(newcurrency) {
    if (!(newcurrency instanceof Currency)) {
      throw new TypeError('Currency must be a currency');
    } else {
      this._currency = newcurrency;
    }
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
